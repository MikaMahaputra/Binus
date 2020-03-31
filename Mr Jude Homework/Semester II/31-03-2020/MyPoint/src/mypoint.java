
public class mypoint {

    private int x = 0;
    private int y = 0;

    public mypoint() {}

    public mypoint(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return this.x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return this.y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public void setXY(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public double distance(int x, int y) {
        int xDiff = this.x - x;
        int yDiff = this.y - y;
        return Math.sqrt(xDiff*xDiff + yDiff*yDiff);
    }

    public double distance(mypoint another) {
        int xDiff = this.x - another.getX();
        int yDiff = this.y - another.getY();
        return Math.sqrt(xDiff*xDiff + yDiff*yDiff);
    }

    public String toString() {
        return "(" + this.x + ", " + this.y + ")";
    }

}   