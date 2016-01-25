// https://www.hackerrank.com/challenges/functional-programming-warmups-in-recursion---gcd

import scala.math._

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

  def main(args: Array[String]): Unit = {
    val lines = io.Source.stdin.getLines()
    val firstLine = lines.next
    val numbers = firstLine.split(" ").map(_.toInt).toList
    println(gcd(numbers(0), numbers(1)))
  }
}
