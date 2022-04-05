export default function cleanSet(set, startString) {
  const arrayToStr = [];
  if (startString.length > 0) {
    for (const value of set) {
      if (value.startsWith(startString)) {
        arrayToStr.push(value.slice(startString.length));
      }
    }
  }
  return arrayToStr.join('-');
}
