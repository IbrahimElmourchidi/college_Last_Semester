const calculator = require('./calculator');

test('add the number to it self', () => {
  expect(calculator.add(2)).toBe(4);
});
