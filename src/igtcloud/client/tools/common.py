import logging
from datetime import datetime
from typing import Iterable, Optional, List, Tuple

import tqdm
from dateutil.parser import parse

from igtcloud.client.services import entities_service
from igtcloud.client.services.entities.model.epd_study import EpdStudy
from igtcloud.client.services.entities.model.file import File
from igtcloud.client.services.entities.model.institute import Institute
from igtcloud.client.services.entities.model.project import Project
from igtcloud.client.services.entities.model.root_study import RootStudy


class TqdmLoggingHandler(logging.Handler):
    def __init__(self, level=logging.NOTSET):
        super().__init__(level)

    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.tqdm.write(msg)
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


def find_project_by_name(project_name: str) -> Optional[Project]:
    projects: Iterable[Project] = entities_service.get_projects()
    projects = filter(lambda p: p.name == project_name, projects)
    for project in projects:
        return project
    return None


def find_institute_by_name(project_id: str, institute_name: str) -> Optional[Institute]:
    institutes: Iterable[Institute] = entities_service.get_institutes(project_id)
    institutes = filter(lambda i: i.name == institute_name, institutes)
    for institute in institutes:
        return institute
    return None


def find_project_and_institutes(project_name: str, institute_name: str = None) -> Tuple[Optional[Project], List[Institute]]:
    institutes = list()
    project = find_project_by_name(project_name)
    if not project:
        return None, institutes

    if institute_name:
        institute = find_institute_by_name(project.id, institute_name)
        if institute:
            institutes.append(institute)
    else:
        institutes = project.institutes

    return project, institutes


def filter_by_ext(ext: Optional[str]):
    if ext is None:
        return None

    def ext_filter(file: File) -> bool:
        return file.type == ext

    return ext_filter


def filter_by_study_date(start: Optional[str], end: Optional[str]):
    if not start and not end:
        return None  # No filtering

    start_d = parse(start).date() if start else datetime(year=1900, month=1, day=1).date()
    end_d = parse(end).date() if end else datetime(year=9999, month=12, day=31).date()

    def date_filter(study: RootStudy) -> bool:
        try:
            if isinstance(study, EpdStudy):
                study_date = study.datetime
            else:
                study_date = study.study_date
            study_date = study_date.date()
            return start_d <= study_date <= end_d
        except Exception:
            return True

    return date_filter


def flatten_dict(input_dict: dict) -> dict:
    output_dict = dict()
    for k, v in input_dict.items():
        if isinstance(v, list):
            output_dict[k] = ', '.join(v)
        elif isinstance(v, dict):
            for kk, vv in flatten_dict(v).items():
                if not kk.startswith(k):
                    kk = k + kk.title()
                output_dict[kk] = vv
        else:
            output_dict[k] = v
    return output_dict


def study_key(study: RootStudy) -> str:
    attr_candidates = ['name', 'clinical_study', 'subject_id']
    for attr in attr_candidates:
        if hasattr(study, attr):
            return getattr(study, attr)
    if hasattr(study, 'patient'):
        return study.patient.patient_name
    else:
        return study.study_database_id
