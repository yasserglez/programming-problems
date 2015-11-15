// https://www.hackerrank.com/challenges/fp-hello-world-n-times

object Solution {

  def f(n: Int) = (1 to n).foreach(i => println("Hello World"))

  def main(args: Array[String]) = {
    io.Source.stdin.getLines().foreach(line => f(line.toInt))
  }
}
