package testing;

public class Thread2 implements Runnable {
public void run(){
int i=1;
while(i<=50)
{
System.out.println(i);
i=i+2;
try
{	
Thread.sleep(300);} 
catch( Exception e ){	};
}
}
public static void main(String[] args)
{
		Thread2 o1 = new Thread2();
		Thread t1= new Thread(o1); 
		t1.start();
}
}
