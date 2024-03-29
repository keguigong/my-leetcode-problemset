/**
 * 斐波那契数
 * https://leetcode.cn/problems/fibonacci-number/
 */

export function fib(n: number): number {
  const dp = []
  dp[0] = 0
  dp[1] = 1
  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2]
  }
  return dp[n]
}

console.log(fib(10))
