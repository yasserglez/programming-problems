// https://www.hackerrank.com/challenges/fp-sum-of-odd-elements

object Solution {
  def f(arr: List[Int]): Int = {
    arr.filter(_ % 2 != 0).sum
  }

  def main(args: Array[String]): Unit = {
    val input = io.Source.stdin.getLines()
    val arr = input.map(_.toInt).toList
    println(f(arr))
  }
}
