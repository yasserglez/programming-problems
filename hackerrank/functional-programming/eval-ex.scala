// https://www.hackerrank.com/challenges/eval-ex

object Solution {

  def factorial(n: Int): Int = {
    n match {
      case 0 => 1
      case _ => n * factorial(n - 1)
    }
  }

  def f(x: Float): Float = {
    1 + (1 to 9).map(k => Math.pow(x, k) / factorial(k)).sum.toFloat
  }

  def main(args: Array[String]): Unit = {
    val lines = io.Source.stdin.getLines()
    val values = lines.drop(1).map(_.toFloat).map(f)
    values.map(value => "%.4f" format value).foreach(println)
  }
}
