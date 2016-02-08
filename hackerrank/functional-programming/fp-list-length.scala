// https://www.hackerrank.com/challenges/fp-list-length

object Solution {
  def f(arr: List[Int]): Int = {
    arr match {
      case Nil => 0
      case (h :: t) => 1 + f(t)
    }
  }

  def main(args: Array[String]): Unit = {
    val input = io.Source.stdin.getLines()
    val arr = input.map(_.toInt).toList
    println(f(arr))
  }
}
