object Timer {
    def oncePerSecond(callback: () => Unit): Unit = {
        while (True) { callback(); Thread sleep 1000 }
    }
    def timeFiles(): Unit = {
        println("time files like an arrow...")
    }
    def main(args: Array[String]): Unit = {
        oncePerSecond(timeFiles)
    }
}