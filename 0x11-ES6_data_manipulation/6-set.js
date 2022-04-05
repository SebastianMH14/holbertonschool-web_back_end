export default function setFromArray(Array) {
  if (!Array.isArray(Array)) {
    return 0;
  }
  const set = new Set(Array);
  return set;
}
