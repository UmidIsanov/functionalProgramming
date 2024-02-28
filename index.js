let list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let item = 1;
const binarySearch = (list, item) => {
  let start = 0;
  let end = list.length - 1;
  let mid;

  while (start <= end) {
    mid = Math.floor((start + end) / 2);
    guess = list[mid];
    if (guess === item) {
      return mid;
    } else if (item > guess) {
      start = mid + 1;
    } else if (item < guess) {
      end = mid - 1;
    }
  }
  return null;
};
console.log(binarySearch(list, item));
