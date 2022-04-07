export default function cleanSet(set, startString) {
  const arrayToStr = [];
  if (startString || typeof(startString) !== 'string') {
    for (const value of set) {
      if (value.startsWith(startString)) {
        arrayToStr.push(value.slice(startString.length));
      }
    }
  }
  return arrayToStr.join('-');
}
