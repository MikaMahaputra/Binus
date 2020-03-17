import java.util.Scanner;

public class class1 {
   
    public static void main(String[] args) {
     
        Scanner s = new Scanner (System.in);
       
        System.out.println("number");
        
        int p = s.nextInt();

        int[] a = new int[p+1];
        int[] b = new int[p+1];
        
        for(int i = 0; i < p; i++)
        {
            a[i] = s.nextInt();
              System.out.println(a[i]);
        }
        int highest=a[0];
        int lowest=a[0];
       
        for(int i = 0; i < p; i++)
        {
        
          if(a[i]>highest)
          {
              highest = a[i];
                    
          }

          if(a[i]<lowest)
          {
              lowest = a[i];             
          } 
        }
          
        int nexthighest=0;
        for(int k = 0; k< p; k++)
        {
           
        if(a[k]<highest)
        {
        nexthighest=a[k];
        break;
      
        }
           
        
        }
    
           for(int i = 0; i < p; i++)
        {
        
          if(a[i]>nexthighest&&a[i]<highest)
          {
              nexthighest = a[i];
                    
          }
        }
           
        
        int x=highest;
        int y=highest-nexthighest;
        int z=nexthighest;
        
        for(int i = 0; i < p+1; i++)
        {
            int z1=p;
            if(a[i]!=highest)
            {
                System.out.print(a[i]+" ");
            }
            else
            {
                a[i]=z;
               
                
              
                System.out.print(a[i]+" ");
                while(z1>i)
                        {
                a[z1]=a[z1-1];
                z1--;
                        }
                a[i+1]=y;
                System.out.print(a[i+1]+" ");
                i++;
                  
            }
        }
     
      
                     
            
             
    }        
}