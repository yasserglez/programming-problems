// https://www.hackerrank.com/challenges/fp-hello-world-n-times

object Solution {

  def f(n: Int) = (1 to n).foreach(i => println("Hello World"))

  def main(args: Array[String]): Unit = {
    val input = io.Source.stdin.getLines()
    input.foreach(line => f(line.toInt))
  }
}
