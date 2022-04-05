export default function cleanSet(set, startString) {
  if (set instanceof Set) {
    if (typeof startString === 'string') {
      const arrayToStr = [];
      if (startString) {
        for (const value of set) {
          if (value.startsWith(startString)) {
            arrayToStr.push(value.slice(startString.length));
          }
        }
      }
      return arrayToStr.join('-');
    }
  }
  return null;
}
