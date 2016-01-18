// https://www.hackerrank.com/challenges/fp-reverse-a-list

object Solution {

  def f(list: List[Int], result: List[Int] = Nil): List[Int] = {
    list match {
      case Nil => result
      case (h :: t) => f(t, h :: result)
    }
  }

  def main(args: Array[String]): Unit = {
    var input = io.Source.stdin.getLines()
    var arr = input.map(_.toInt).toList
    f(arr).foreach(println)
  }
}
