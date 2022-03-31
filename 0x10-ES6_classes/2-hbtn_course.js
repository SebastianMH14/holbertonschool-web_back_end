export default class HolbertonCourse {
  constructor(name = '', length = 0, students = []) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    } else { this._name = name; }

    if (typeof length !== 'number') {
      throw TypeError('Length must be a number');
    } else {
      this._length = length;
    }

    if (Array.isArray(students)) {
      this._students = students;
    } else {
      throw TypeError('Students must be a array of Strings');
    }
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  get length() {
    return this._length;
  }

  set length(length) {
    if (typeof length === 'number') {
      this._length = length;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  get students() {
    return this._students;
  }

  set students(students) {
    if (Array.isArray(students)) {
      this._students = students;
    } else {
      throw TypeError('Students must be a array of Strings');
    }
  }
}
