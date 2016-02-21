// http://www.hackerrank.com/challenges/common-divisors

import math._

object Solution {

  def gcd(x: Int, y: Int): Int = {
    if (x != y) {
      val m = min(x, y)
      val M = max(x, y)
      gcd(M - m, m)
    } else {
      x
    }
  }

  def commonDivisors(x: Int, y: Int): Int = {
    var count = 0;
    for (k <- 1 to gcd(x, y)) {
      if (x % k == 0 && y % k == 0) count += 1;
    }
    count
  }

  def main(args: Array[String]): Unit = {
    val lines = io.Source.stdin.getLines()
    val testCases = lines.next.toInt
    for (i <- 1 to testCases) {
      val numbers = lines.next.split(" ").map(_.toInt).toList
      println(commonDivisors(numbers(0), numbers(1)))
    }

  }
}
