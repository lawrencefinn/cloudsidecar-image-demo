lazy val root = (project in file("."))
  .enablePlugins(PlayScala)
  .settings(
    name := """play-upload""",
    version := "1.0-SNAPSHOT",
    scalaVersion := "2.13.1",
    libraryDependencies ++= Seq(
      ws,
      guice,
      "com.github.seratch" %% "awscala" % "0.8.+",
      "org.scalatestplus.play" %% "scalatestplus-play" % "5.0.0" % Test
    ),
    scalacOptions ++= Seq(
      "-feature",
      "-deprecation",
      "-Xfatal-warnings"
    )
  )
