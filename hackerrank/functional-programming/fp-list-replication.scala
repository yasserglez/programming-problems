// https://www.hackerrank.com/challenges/fp-list-replication

object Solution {
  def f(num: Int, arr: List[Int]): List[Int] = {
    arr.flatMap(x => List.fill(num)(x))
  }

  def main(args: Array[String]): Unit = {
    val input = io.Source.stdin.getLines()
    val num = input.take(1).map(_.toInt).next()
    var arr = input.map(_.toInt).toList
    f(num, arr).foreach(println)
  }
}
