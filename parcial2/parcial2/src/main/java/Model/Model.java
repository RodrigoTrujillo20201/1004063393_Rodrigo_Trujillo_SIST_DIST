package Model;

import Conexion.Conexion;
import Interface.CRUD;

import java.sql.Connection;
import java.sql.ResultSet;

/**
 *
 * @author ariel
 */
public class Model implements CRUD{

    public static void setNombreCompleto(int nombreCompleto) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
    Conexion conn = new Conexion();
    private int numeroGrupo;


    
    public int getNumeroGrupo() {
        return numeroGrupo;
    }

    public void setNumeroGrupo(int numeroGrupo) {
        this.numeroGrupo = numeroGrupo;
    }

    
  
    
    @Override
    public void Agregar() {
        // Establecer la conexión
        conn.conectar();
        
         // Puedes realizar operaciones en la base de datos aquí, por ejemplo:
        String sql = "INSERT INTO grupo (nombre_completo) VALUES ("+this.nombre_completo()+")";
        
        conn.ejecutarUpdate(sql);
        
        // Cerrar la conexión
        conn.cerrarConexion();
    }

    public void Modificar() {
            conn.conectar();
               String sql = "UPDATE grupo (nombre_completo) VALUES ("+this.nombre_completo()+")";
                conn.ejecutarUpdate(sql);
        
        // Cerrar la conexión
        conn.cerrarConexion();
    }
     
        
        
    

       @Override
    public void Eliminar() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }

    @Override
    public Object Consultar() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
        
         // Realizar una consulta y obtener datos
        //ResultSet resultSet = conexion.ejecutarQuery("SELECT * FROM grupo");
    }

    @Override
    public Object ConsultarId() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }

    private String getNombreCompleto() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    private String nombre_completo() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
}
