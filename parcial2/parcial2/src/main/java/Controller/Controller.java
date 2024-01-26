
package Controller;

import Model.Model;

/**
 *
 * @author ariel
 */
public class Controller {
    public void Agregar(int nombreCompleto){
        //Objeto del modelo
        Model Model = new Model();
        Model.setNombreCompleto(nombreCompleto);
        Model.Agregar();
    }
}