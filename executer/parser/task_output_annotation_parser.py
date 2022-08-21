from json import loads


class TaskOutputAnnotationParser():
    def __init__(self, raw_output_annotations_str: str):
        self.raw_output_annotations_str = raw_output_annotations_str
        for k, v in loads(raw_output_annotations_str).items():
            self.__dict__[k] = int(v)

    def __str__(self):
        return self.raw_output_annotations_str