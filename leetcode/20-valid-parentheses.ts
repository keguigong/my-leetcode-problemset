/**
 * https://leetcode.cn/problems/valid-parentheses/
 */

function isValid(s: string): boolean {
  let len = s.length;
  if (len % 2 !== 0) return false;

  while (/\(\)/.test(s) || /\[\]/.test(s) || /\{\}/.test(s)) {
    s = s.replace("()", "");
    s = s.replace("[]", "");
    s = s.replace("{}", "");
  }

  return s === "";
}

let brackets = "([])";
console.log(isValid(brackets));