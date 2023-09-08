import io
from typing import Optional


class S3File(io.RawIOBase):
    def __init__(self, s3_client, bucket, key, mode):
        self._s3_client = s3_client
        self._bucket = bucket
        self._key = key
        self._position: int = 0
        self.mode = mode

    def __repr__(self):
        return "<%s s3_object=%s/%s>" % (type(self).__name__, self._bucket, self._key)

    def readinto(self, buffer) -> Optional[int]:
        data = self.read(len(buffer))
        buffer[:len(data)] = data
        return len(data)

    def read(self, size: int = -1) -> Optional[bytes]:
        self._checkClosed()
        if self._position >= self.size:
            return bytes()
        if size == -1:
            # Read to the end of the file
            range_header = "bytes=%d-" % self._position
            self.seek(offset=0, whence=io.SEEK_END)
        else:
            new_position = self._position + size

            # If we're going to read beyond the end of the object, return
            # the entire object.
            if new_position >= self.size:
                return self.read()

            range_header = "bytes=%d-%d" % (self._position, new_position - 1)
            self.seek(offset=size, whence=io.SEEK_CUR)

        return self._s3_client.get_object(Bucket=self._bucket, Key=self._key, Range=range_header)["Body"].read()

    def readable(self) -> bool:
        return True

    def seek(self, offset: int, whence: int = io.SEEK_SET) -> int:
        self._checkClosed()
        if whence == io.SEEK_SET:
            self._position = offset
        elif whence == io.SEEK_CUR:
            self._position += offset
        elif whence == io.SEEK_END:
            self._position = self.size + offset
        else:
            raise ValueError("invalid whence (%r, should be %d, %d, %d)" % (
                whence, io.SEEK_SET, io.SEEK_CUR, io.SEEK_END
            ))

        return self._position

    def seekable(self) -> bool:
        return True

    def tell(self) -> int:
        self._checkClosed()
        return self._position

    @property
    def size(self) -> int:
        return self._s3_object.content_length

    @property
    def name(self) -> str:
        return self._s3_object.key
