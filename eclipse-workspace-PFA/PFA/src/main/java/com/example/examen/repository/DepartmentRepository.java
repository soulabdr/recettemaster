package com.example.examen.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.example.examen.models.Department;

@Repository
public interface DepartmentRepository extends CrudRepository<Department, Long> {
    // Additional methods if needed
}