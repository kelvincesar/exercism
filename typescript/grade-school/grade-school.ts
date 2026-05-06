type StudentName = string;
type Grade = number;
type SchoolRoster = Record<number, StudentName[]>;


export class GradeSchool {
  private studentsByGrade: SchoolRoster = {};

  roster(): SchoolRoster {
    const schoolRoster: SchoolRoster = {};

    for (const [grade, students] of Object.entries(this.studentsByGrade)) {
      schoolRoster[Number(grade)] = [...students];
    }

    return schoolRoster;
  }

  add(name: StudentName, grade: Grade) {
    this.removeStudent(name);

    const students = this.studentsByGrade[grade] ?? [];
    this.studentsByGrade[grade] = [...students, name].sort();
  }

  grade(grade: Grade) {
    return [...(this.studentsByGrade[grade] ?? [])];
  }

  private removeStudent(name: StudentName) {
    for (const [grade, students] of Object.entries(this.studentsByGrade)) {
      const updatedStudents = students.filter((student) => student !== name);

      if (updatedStudents.length === 0) {
        delete this.studentsByGrade[Number(grade)];
      } else {
        this.studentsByGrade[Number(grade)] = updatedStudents;
      }
    }
  }
}
