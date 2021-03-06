from manim import *

# Link to video: https://www.youtube.com/watch?v=htjV5RZkhjA&t=3s

class ChainRule(Scene):
  def construct(self):

    pt1a = MathTex("\\text{According to the chain rule, the derivative of } ", "g(", "h(", "x", ")", ")", "\\text{ is...}")
    pt1b = MathTex("\\text{According to the chain rule, the derivative of } ", "g(", "h(", "x", ")", ")", "\\text{ is...}").scale(0.75).to_edge(UL)
    pt1c = MathTex(r"\frac{dg}{dx}", " = ", r"\frac{dg}{dh}", r"\times", r"\frac{dh}{dx}").scale(1.5)
    pt1d = MathTex("\\underline{\\text{Example :}}").scale(0.75).to_edge(UL)
    pt1e = MathTex("\\text{Say we have the following function...}").scale(0.75).to_edge(UP).shift(DOWN)
    pt1f = MathTex(r"(", r"3\sin x + 1", r")^5").scale(1.5)
    pt1g = MathTex("\\text{We can interpret this as two nested functions...}").scale(0.75).to_edge(UP).shift(DOWN)
    pt1h = MathTex("\\text{The outside being }", r"g(x) = x^5", "\\text{...}").scale(0.75).to_edge(UP).shift(DOWN)
    pt1i = MathTex("\\text{And the inner function being }", r"3\sin x + 1", "\\text{...}").scale(0.75).to_edge(UP).shift(DOWN)
    pt1j = MathTex("\\text{The key is to notice that the inner function is like the x value of the outside...}").set_color(YELLOW).scale(0.60).to_edge(DOWN).shift(UP)
    pt1k = MathTex("\\text{Regardless of what's inside, it's just a value that is being raised to the power of 5...}").set_color(YELLOW).scale(0.60).to_edge(DOWN).shift(UP)
    pt1l = MathTex("\\text{So, we must take the derivative of the outside with respect to its input...}").scale(0.75).to_edge(UP).shift(DOWN)
    pt1m = MathTex("\\text{And multiply it by the derivative of the inside with respect to its input...}").scale(0.75).to_edge(UP).shift(DOWN)
    pt1n = MathTex(r"5(", r"3\sin x + 1", r")^4").scale(1.5)
    pt1o = MathTex(r"5(", r"3\sin x + 1", r")^4", r"3\cos x").scale(1.5)
    pt1p = MathTex("\\text{But why does this work?}").scale(0.75).to_edge(UP).shift(DOWN)

    pt1h[1].set_color(RED)
    pt1i[1].set_color(BLUE)

    pt1f[0].set_color(RED)
    pt1f[1].set_color(BLUE)
    pt1f[2].set_color(RED)
    pt1n[0].set_color(RED)
    pt1n[1].set_color(BLUE)
    pt1n[2].set_color(RED)
    pt1o[0].set_color(RED)
    pt1o[1].set_color(BLUE)
    pt1o[2].set_color(RED)
    pt1o[3].set_color(BLUE)

    pt1a[1].set_color(RED)
    pt1a[2].set_color(BLUE)
    pt1a[3].set_color(BLUE)
    pt1a[4].set_color(BLUE)
    pt1a[5].set_color(RED)

    pt1b[1].set_color(RED)
    pt1b[2].set_color(BLUE)
    pt1b[3].set_color(BLUE)
    pt1b[4].set_color(BLUE)
    pt1b[5].set_color(RED)

    pt1c[0][0:3].set_color(RED)
    pt1c[0][3:5].set_color(YELLOW)
    pt1c[2][0:3].set_color(RED)
    pt1c[2][3:5].set_color(BLUE)
    pt1c[4][0:3].set_color(BLUE)
    pt1c[4][3:5].set_color(YELLOW)

    
    
    self.play(Write(pt1a))
    self.wait()
    self.play(Transform(pt1a, pt1b))
    self.wait()
    self.play(Write(pt1c))
    self.wait(4)
    self.play(FadeOut(pt1a),FadeOut(pt1c))
    self.play(Write(pt1d))
    self.wait()
    self.play(Write(pt1e))
    self.wait(2)
    self.play(Write(pt1f))
    self.wait(3)
    self.play(Transform(pt1e, pt1g))
    self.wait(3)
    self.play(Transform(pt1e, pt1h))
    self.wait(3)
    self.play(Transform(pt1e, pt1i))
    self.wait(3)
    self.play(Write(pt1j))
    self.wait(3)
    self.play(Transform(pt1j, pt1k))
    self.wait(4)
    self.play(Transform(pt1e, pt1l))
    self.wait(3)
    self.play(Transform(pt1f, pt1n))
    self.wait(3)
    self.play(Transform(pt1e, pt1m))
    self.wait(3)
    self.play(Transform(pt1f, pt1o))
    self.wait(4)
    self.play(Transform(pt1e, pt1p))
    self.wait(3)

    self.play(FadeOut(pt1d),FadeOut(pt1e),FadeOut(pt1f),FadeOut(pt1j),FadeOut(pt1o))
    self.wait()

    pt2a = MathTex("\\text{Well, let's start by looking at how }", "h(x)", "\\text{ changes...}")
    pt2b = MathTex("\\text{Well, let's start by looking at how }", "h(x)", "\\text{ changes...}").scale(0.75).to_edge(UL)
    pt2c = MathTex("\\text{If we change } x \\text{ by a tiny amount } ", "dx", "\\text{, how does }", "h(x)", "\\text{ change?}").scale(0.75).to_edge(UL)
    pt2d = MathTex("\\text{Let's call this change }", "dh", "\\text{, so...}").scale(0.75).to_edge(UL)
    pt2e = MathTex("dh", " = ", "h'(", "x", ")", "dx" ).scale(1.5)
    pt2f = MathTex("\\text{Note that } ", "dx", "\\text{ is an infinitesimally small value...}").scale(0.75).to_edge(DOWN).shift(UP)
    pt2g = MathTex("\\text{This means that the change in }", "h(x)", "\\text{ is equal to its rate of change...}").scale(0.75).to_edge(UL)
    pt2h = MathTex("\\text{And proportional to the tiny change in x, }", r"\dd x", "\\text{, which is almost negligble...}").scale(0.75).to_edge(UL)

    pt2a[1].set_color(BLUE)
    pt2b[1].set_color(BLUE)
    pt2c[1].set_color(YELLOW)
    pt2c[3].set_color(BLUE)
    pt2d[1].set_color(BLUE)

    pt2e[0].set_color(BLUE)
    pt2e[2].set_color(BLUE)
    pt2e[3].set_color(YELLOW)
    pt2e[4].set_color(BLUE)
    pt2e[5].set_color(YELLOW)

    pt2f[1].set_color(YELLOW)
    pt2g[1].set_color(BLUE)
    pt2h[1].set_color(YELLOW)

    self.play(Write(pt2a))
    self.wait(3)
    self.play(Transform(pt2a, pt2b))
    self.wait()
    self.play(Transform(pt2a, pt2c))
    self.wait(4)
    self.play(Transform(pt2a, pt2d))
    self.wait(2)
    self.play(Write(pt2e))
    self.wait(3)
    self.play(Write(pt2f))
    self.wait(4)
    self.play(FadeOut(pt2f))
    self.play(Transform(pt2a, pt2g))
    self.wait(5)
    self.play(Transform(pt2a, pt2h))
    self.wait(5)

    self.play(FadeOut(pt2a),FadeOut(pt2e))
    self.wait()

    pt3a = MathTex("\\text{Now let's look at how }", "g", "\\text{ changes...}")
    pt3b = MathTex("\\text{Now let's look at how }", "g", "\\text{ changes...}").scale(0.75).to_edge(UL)
    pt3c = MathTex("\\text{The change in }", "g", "\\text{ is its rate of change, with respect to its input, }", "h(x)", "\\text{...}").scale(0.75).to_edge(UL)
    pt3z = MathTex("\\text{And proportional to the change in its input, }", "dh", "\\text{, which we have calculated...}").scale(0.75).to_edge(UL)
    pt3d = MathTex("\\text{So we can let }", "k = h(x)", "\\text{ to make things more obvious...}").scale(0.75).to_edge(UL)
    pt3e = MathTex("\\text{And let the change in }", "g", "\\text{ be }", "dg", "\\text{...}").scale(0.75).to_edge(UL)
    pt3f = MathTex("dg", " = ", "g'(", "k", ")", "dk").scale(1.5)
    pt3g = MathTex("dg", " = ", "g'(", "h(", "x", ")", ")", "dh").scale(1.5)
    pt3h = MathTex("\\text{So expanding again...}").scale(0.75).to_edge(UL)
    pt3i = MathTex("\\text{This means the change in }", "g", "\\text{ is determined by the change in }", "h", "\\text{...}").scale(0.75).to_edge(UL)
    pt3j = MathTex("\\text{But we know how }", "h", "\\text{ changes with respect to x...}").scale(0.75).to_edge(UL)
    pt3k = pt2e.scale(0.60).to_edge(DOWN).shift(UP)
    pt3l = MathTex("\\text{So we can simply expand }", "dh", "\\text{...}").scale(0.75).to_edge(UL)
    pt3m = MathTex("dg", " = ", "g'(", "h(", "x", ")", ")", "h'(", "x", ")", "dx").scale(1.5)
    pt3n = MathTex(r"\frac{dg}{dx}", " = ", "g'(", "h(", "x", ")", ")", "h'(", "x", ")").scale(1.5)
    pt3o = MathTex("\\text{And rearranging...}").scale(0.75).to_edge(UL)
    pt3p = MathTex("\\text{This is the chain rule!}").scale(0.75).to_edge(UL)

    pt3a[1].set_color(RED)
    pt3b[1].set_color(RED)
    pt3c[1].set_color(RED)

    pt3c[3].set_color(BLUE)
    pt3d[1].set_color(BLUE)

    pt3z[1].set_color(BLUE)

    pt3e[1].set_color(RED)
    pt3e[3].set_color(RED)
    pt3f[1].set_color(RED)
    pt3f[3].set_color(RED)

    pt3f[0].set_color(RED)
    pt3f[2].set_color(RED)
    pt3f[3].set_color(BLUE)
    pt3f[4].set_color(RED)
    pt3f[5].set_color(BLUE)

    pt3g[0].set_color(RED)
    pt3g[2].set_color(RED)
    pt3g[3].set_color(BLUE)
    pt3g[4].set_color(YELLOW)
    pt3g[5].set_color(BLUE)
    pt3g[6].set_color(RED)
    pt3g[7].set_color(BLUE)

    pt3i[1].set_color(RED)
    pt3i[3].set_color(BLUE)
    pt3j[1].set_color(BLUE)
    pt3l[1].set_color(BLUE)

    pt3m[0].set_color(RED)
    pt3m[2].set_color(RED)
    pt3m[3].set_color(BLUE)
    pt3m[4].set_color(YELLOW)
    pt3m[5].set_color(BLUE)
    pt3m[6].set_color(RED)
    pt3m[7].set_color(BLUE)
    pt3m[8].set_color(YELLOW)
    pt3m[9].set_color(BLUE)
    pt3m[10].set_color(YELLOW)

    pt3n[0][0:3].set_color(RED)
    pt3n[0][3:5].set_color(YELLOW)
    pt3n[2].set_color(RED)
    pt3n[3].set_color(BLUE)
    pt3n[4].set_color(YELLOW)
    pt3n[5].set_color(BLUE)
    pt3n[6].set_color(RED)
    pt3n[7].set_color(BLUE)
    pt3n[8].set_color(YELLOW)
    pt3n[9].set_color(BLUE)

    self.play(Write(pt3a))
    self.wait(2)
    self.play(Transform(pt3a, pt3b))
    self.wait()
    self.play(Transform(pt3a, pt3c))
    self.wait(5)
    self.play(Transform(pt3a, pt3z))
    self.wait(5)
    self.play(Transform(pt3a, pt3d))
    self.wait(4)
    self.play(Transform(pt3a, pt3e))
    self.wait()
    self.play(Write(pt3f))
    self.wait(4)
    self.play(Transform(pt3a, pt3h))
    self.wait()
    self.play(Transform(pt3f, pt3g))
    self.wait()
    self.play(Transform(pt3a, pt3i))
    self.wait(5)
    self.play(Transform(pt3a, pt3j))
    self.wait(4)
    self.play(Write(pt3k))
    self.wait(4)
    self.play(Transform(pt3a, pt3l))
    self.wait()
    self.play(Transform(pt3f, pt3m))
    self.wait(5)
    self.play(Transform(pt3a, pt3o))
    self.wait()
    self.play(Transform(pt3f, pt3n))
    self.wait(4)
    self.play(Transform(pt3a, pt3p))
    self.wait(4)
