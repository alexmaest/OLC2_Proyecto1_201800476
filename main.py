from Grammar.parser import startParser
#let SingleA1 : [i64;5] = 30;
#println!(SingleA1);
s = '''
    fn Main() {
        println!("Desde el Main");
        let varX : i64 = 9;
        let alex = ["single" + 5; 3 +3 ];
        let single = -4;
        let single2 = "Hola"+single;
        single1(varX);
    }

    fn single1(var1 : i64){
        println!("Hola desde single1");
        println!(var1);
        match var1 {
            1 | 2 => {
                let x = 100;
                println!("Rango de 1 a 3: "+x);
            },
            6 | 7 | 8 => println!("Rango de 6 a 8"),
            _ =>println!("Si o si"),
        }
    }

    fn single2(){
        println!("Hola desde single2");
        let letsTry = true;
        let letsTry2 = true;
        if letsTry && letsTry2 {
            let letsTry3 = false;
            println!("Hola desde if");
        } else if letsTry || letsTry2 {
            println!("Hola desde else if");
        } else{
            println!("Hola desde else");
        }
        let counter = 0;
        while counter == 6 {
            println!("Hola desde while");
            if counter == 4 {
                println!("Continue ;)");
                counter = counter + 1;
                continue;
            } else{
                println!("Contador: " + counter);
            }
            counter = counter + 1;
        }
        let infinite = 0;
        loop {
            if infinite == 100 {
                println!("Break ;)");
                break;
            }else if infinite == 50 {
                infinite = infinite + 1;
                continue;
            }else{
                println!("infinite: "+infinite);
                infinite = infinite + 1;
            }
        }
    }
'''
startParser(s)