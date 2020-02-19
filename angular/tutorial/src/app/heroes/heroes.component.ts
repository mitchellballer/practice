import { Component, OnInit } from '@angular/core';

import { Hero } from '../hero';
import { HeroService } from '../hero.service';
import { MessageService } from '../message.service';

@Component({
  selector: 'app-heroes',
  templateUrl: './heroes.component.html',
  styleUrls: ['./heroes.component.css'],
})

export class HeroesComponent implements OnInit {

  heroes: Hero[];
  selectedHero: Hero;

  constructor(private heroService: HeroService, private messageService: MessageService) {}

  onSelect(hero: Hero): void {
    this.selectedHero = hero;
    this.messageService.add('HeroService: Selected hero id=${hero.id}');
  }
  
  hero: Hero = {
    id: 1,
    name: "Windstorm",
  };

  getHeroes(): void {
    this.heroService.getHeroes()
      .subscribe(heroes => this.heroes = heroes);
  }
  
  ngOnInit() {
    this.getHeroes();
  }



}
