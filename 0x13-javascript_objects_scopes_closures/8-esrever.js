#!/usr/bin/node

// function that reverses a lists.
exports.esrever = function (list) {
  if (!list) return (undefined);
  for (let i = 0, j = list.length - 1; i < j; i++, j--) {
    const tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
  }

  return (list);
};
