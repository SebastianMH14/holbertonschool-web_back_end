const weakMap = new WeakMap();
let count = 1;

function queryAPI(endpoint) {
  weakMap.set(endpoint, count);
  count += 1;
  if (count >= 5) {
    throw new Error('Endpoint load is high');
  }
}

export { queryAPI, weakMap };
