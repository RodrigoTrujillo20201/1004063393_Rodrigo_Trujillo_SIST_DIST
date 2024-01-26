package Interface;

/**
 *
 * @author ariel
 */
public interface CRUD {
    
    //Método para agregar
    public void Agregar();
    
    //Método para modificar
    public void Modificar();
    
    //Método para eliminar
    public void Eliminar();
    
    //Método para agregar
    public Object Consultar();
    
    //Método para Consultar por id
    public Object ConsultarId();
}
