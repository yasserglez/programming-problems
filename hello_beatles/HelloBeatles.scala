object HelloBeatles {
  def main(args: Array[String]) {
    io.Source.stdin.getLines().foreach(name => println("Hello, " + name + "!"))
  }
}
