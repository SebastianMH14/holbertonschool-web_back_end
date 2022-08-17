export default function cleanSet(set, startString = '') {
  const array = [];
  if (startString.length === 0 || typeof startString !== 'string') return '';
  set.forEach((element) => {
    if (element.startsWith(startString)) {
      array.push(element.slice(startString.length));
    }
  });
  set.clear();
  return array.join('-');
}
