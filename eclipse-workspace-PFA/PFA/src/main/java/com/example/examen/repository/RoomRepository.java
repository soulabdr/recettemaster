package com.example.examen.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.example.examen.models.Room;

@Repository
public interface RoomRepository extends CrudRepository<Room, Long> {
    // Additional methods if needed
}
