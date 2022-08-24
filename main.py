from Grammar.parser import startParser
#mut x -> mut x :[i64;3]
#&mut x -> x : &mut[i64;3]
#x -> x : [i64;3]
#&mut x -> mut x : &[i64;3]
#&mut x -> x : &[i64;3]
s = '''
    fn Main() {
        println!("Desde el Main");
        let str1 : [string;2] = ["Hola".to_string(),"Hola".to_string()];
        let str2 : &str = "pana";
        println!(str1);
        println!(str2);
        let varX : [i64;3] = [1,2,3];
        let mut alex = [5 ; 3];
        println!(varX);
        println!(alex);
        alex = [10,20,30];
        println!(alex);
        println!(varX);
        singleOne(varX);
        println!(varX);
    }

    fn suma(x : i64, y: i64) -> i64{
        println!("Hola desde suma");
        println!(x);
        println!(y);
        return x + y;
    }

    fn singleOne(x: [i64;3]){
        println!(x);
        x = [5,6,7];
        println!(x);
    }

    fn single1(var1 : i64){
        println!("Hola desde single1");
        println!(var1);
        match var1 {
            1 | 2 => {
                let x = 100;
                println!("Rango de 1 a 3: ");
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
                println!("infinite: ");
                infinite = infinite + 1;
            }
        }
    }
'''
startParser(s)