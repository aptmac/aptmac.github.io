---
layout: post
title:  "How to install the JDK Mission Control Agent in Fedora via COPR"
date:   2021-12-14 22:33:55 -0400
categories: jmc
---

In a previous post [link](https://aptmac.github.io/jmc/2021/09/14/copr-jmc.html), I wrote about how to install JMC on Fedora via copr. I'm back with an update; the JMC Agent (v.1.0.1) is now available through copr as well!

One of the big features included in the JMC 8.1.0 release was the JMC agent plugin, which provides a user-interface for interacting with the JMC agent. The agent itself can be used to add custom Flight Recorder events to a Java program already in execution. The current issue is that the agent does not ship alongside JMC, and needs to be built separately from sources and imported into the JMC application. As a result, if you downloaded my JMC builds via copr, the only way to use the agent plugin would be to either build the agent yourself, or by finding a jar floating on the internet.

But, as the title of this blog post suggests, the agent can now be installed via copr as well! I have a copr repo set up [https://copr.fedorainfracloud.org/coprs/almac/jmc-agent/](https://copr.fedorainfracloud.org/coprs/almac/jmc-agent/), with builds currently for Fedora 34/35/Rawhide that can be installed using the following commands:


{% highlight bash %}
// 1. enable the copr repo
$ dnf copr enable almac/jmc-agent

// 2. install the jmc
$ sudo dnf install jmc-agent

// the agent jar will now be installed at /usr/share/java/jmc-agent/agent.jar
{% endhighlight %}

Now that you have the agent jar on your system, you can hook it up with JMC and start using the JMC agent plugin! Now, I could spend some time here and explain some of the features and basic instructions on how to use it .. or I could refer you to some great articles written by my colleagues, be sure to check them out!

JVM performance monitoring with JMC agent: [https://developers.redhat.com/articles/2021/11/16/jvm-performance-monitoring-jmc-agent](https://developers.redhat.com/articles/2021/11/16/jvm-performance-monitoring-jmc-agent)

Collect JDK Flight Recorder events at runtime with JMC Agent: [https://developers.redhat.com/blog/2020/10/29/collect-jdk-flight-recorder-events-at-runtime-with-jmc-agent](https://developers.redhat.com/blog/2020/10/29/collect-jdk-flight-recorder-events-at-runtime-with-jmc-agent)
