from Grammar.parser import startParser
#let SingleA1 : [i64;5] = 30;
#println!(SingleA1);
s = '''
    fn Main() {
        println!("Hola desde el Main");
        let varX : i64 = 15;
        let alex = ["hola pai"+5;3+3];
        println!(alex);
        alex = ["XD"];
        let single = -4;
        let single2 = "Hola"+single;
        println!(single2);
        println!(alex);
        single1(varX);
    }

    fn single1(var1 : i64){
        println!("Hola desde single1");
        println!(var1);
        single2();
    }

    fn single2(){
        println!("Hola desde single2");
    }
'''
startParser(s)