from typing import Dict, Optional
from dataclasses import dataclass


@dataclass
class Submission:
    time: str
    memory: int
    stdout: Optional[str]
    stderr: Optional[str]
    compile_output: Optional[str]

    @classmethod
    def from_dict(cls, dikt) -> "Submission":
        return cls(
            time=dikt["time"],
            memory=dikt["memory"],
            stdout=dikt["stdout"] if dikt.get("stdout") else None,
            stderr=dikt["stderr"] if dikt.get("stderr") else None,
            compile_output=dikt["compile_output"]
            if dikt.get("compile_output")
            else None,
        )
