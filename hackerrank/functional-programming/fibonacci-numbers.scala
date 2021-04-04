// http://www.hackerrank.com/challenges/functional-programming-warmups-in-recursion---fibonacci-numbers

object Solution {

  val numbers: LazyList[Int] = 0 #:: 1 #:: (numbers zip numbers.tail).map(l => l._1 + l._2)

  def fibonacci(n: Int): Int = {
    numbers.drop(n - 1).head
  }

  def main(args: Array[String]): Unit = {
    val lines = io.Source.stdin.getLines()
    println(fibonacci(lines.next().toInt))
  }
}
