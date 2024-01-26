package Entities;

import java.time.LocalDateTime;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "product_1004063393")
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "nombre", length = 11, nullable = false, unique = true)
    private String nombre;
    
    @Column(name = "description", length = 200, nullable = false)
    private String description;
    
    @Column(name = "estado", nullable = true)
    private Boolean estado;
    
    @Column(name = "fecha_creacion", nullable = true)
    private LocalDateTime fechaCreacion;
    
    @Column(name = "fecha_modificacion", nullable = true)
    private LocalDateTime fechaModificacion;
    
    @Column(name = "fecha_eliminacion", nullable = true)
    private LocalDateTime fechaEliminacion;    
    
    @Column(name = "product_creacion", nullable = true)
    private Long productCreacion;
    
    @Column(name = "product_modificacion", nullable = true)
    private Long productModificacion;
    
    @Column(name = "productEliminacion", nullable = true)
    private Long productEliminacion;
    
}