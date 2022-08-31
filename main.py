from Grammar.parser import startParser
#mut x -> mut x :[i64;3]
#&mut x -> x : &mut[i64;3]
#x -> x : [i64;3]
#&mut x -> mut x : &[i64;3]
#&mut x -> x : &[i64;3]
#Acceder a funciones de mods?
s = '''
    mod Vehiculos{
        pub mod Carros{
            pub struct Automovil{
                pub id : i64,
                pub precio : i64,
                pub marca : Compania
            }
            pub fn getLanchas() -> &str{
                println!("Hola desde getLanchas()");
                return "Este es el return de lanchas pana";
            }
        }
        pub fn getVehiculos() -> &str{
            println!("Hola desde getVehiculos()");
            return "Este es el return vehiculos pana";
        }
    }

    struct Compania{
        pub fundacion : i64,
        pub nombre : String
    }

    fn main() {
        println!("{}",f64::powf(3.0,2.0));
        let singleArr: Vec<i64> = Vec::with_capacity(20);
        println!("{}",singleArr.capacity());
        let variableC = 50.0 as i64;
        println!("{}",variableC);
        let booleanS = true;
        let proofS = if booleanS{
            println!("Hola desde if");
            10
        };
        println!("{}",proofS);
        println!("Desde el Main");
        let mut auto1 = Vehiculos::Carros::Automovil{id:1, precio:300000, marca:Compania{fundacion:1920,nombre:"Ferrari".to_string()}};
        let mut auto2 = Vehiculos::Carros::Automovil{id:2, precio:20000, marca:Compania{fundacion:1890,nombre:"Lotus".to_string()}};
        println!("{}",auto2.id);
        println!("{}",auto2.precio);
        println!("{}",auto2.marca.nombre);
        println!("{}",auto2.marca.nombre.to_string());
        let getText = Vehiculos::getVehiculos();
        println!("{}",getText);
        let getText2 = Vehiculos::Carros::getLanchas();
        println!("{}",getText2);
        let str1 : [String;2] = ["Hola".to_string(),"Hola".to_string()];
        let str2 : &str = "pana";
        println!("{:?}",str1);
        println!("{}",str2);
        auto1.id = 100;
        let mut varX : [i64;3] = [1,2,3];
        let mut alex = [5 ; 3];
        println!("{:?}",varX);
        println!("{:?}",alex);
        alex = [10,20,30];
        println!("{:?}",alex);
        println!("{:?}",varX);
        singleOne(mut varX);
        println!("{:?}",varX);
        let singleSuma = suma(10,20);
        println!("{}",singleSuma);
        let proof : usize = 0;
        println!("{}",proof);
    }

    fn suma(x : i64, y: i64) -> i64{
        println!("Hola desde suma");
        println!("{}",x);
        println!("{}",y);
        return x + y;
    }

    fn singleOne(mut x: [i64;3]){
        println!("{:?}",x);
        x = [5,6,7];
        println!("{:?}",x);
    }

    fn single1(var1 : i64){
        println!("Hola desde single1");
        println!("{}",var1);
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
                println!("{}",counter);
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