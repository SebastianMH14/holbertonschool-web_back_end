export default class Building {
  constructor(sqft) {
    if (typeof sqft === 'number') {
      this._sqft = sqft;
    } else {
      throw TypeError('Sqft must be a number');
    }
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    if (this.constructor !== Building) {
      throw new Error(
        'Class extending Building must override evacuationWarningMessage',
      );
    }
  }
}
