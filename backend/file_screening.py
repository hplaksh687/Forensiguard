def detect_multi_extension(filename):
    parts = filename.split(".")
    if len(parts) > 2:
        return True
    return False

try:
    import magic
    def verify_file_type(file_path):
        mime = magic.Magic(mime=True)
        return mime.from_file(file_path)
except ImportError:
    def verify_file_type(file_path):
        ext = file_path.split(".")[-1].lower()
        mapping = {"mp4": "video/mp4", "avi": "video/avi",
                   "mov": "video/quicktime", "wav": "audio/wav", "mp3": "audio/mpeg"}
        return mapping.get(ext, "unknown")
