object HelloBeatles {
  def main(args: Array[String]): Unit = {
    val input = io.Source.stdin.getLines()
    input.foreach(name => println("Hello, " + name + "!"))
  }
}
