CREATE DATABASE `football-club` /*!40100 DEFAULT CHARACTER SET latin1 */;

CREATE TABLE `roles` (
  `role_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='admin, coach, player.. São funções para conseguir atribuir funcionalidades';

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `users_FK` (`role_id`),
  CONSTRAINT `users_FK` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Tabela de Usuários';

CREATE TABLE `teams` (
  `team_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `image_url` varchar(500) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Será a tabela dos times';

CREATE TABLE `tournaments` (
  `tournament_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(155) DEFAULT NULL,
  `image_url` varchar(500) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  PRIMARY KEY (`tournament_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='amistoso, São Pedro Amador, Santa Olimpia';

CREATE TABLE `players` (
  `player_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `team_id` int(11) DEFAULT NULL,
  `nickname` varchar(100) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `image_url` varchar(500) DEFAULT NULL,
  `description` text,
  `main_position` varchar(30) DEFAULT NULL,
  `secondary_position` varchar(30) DEFAULT NULL,
  `signed` tinyint(1) DEFAULT NULL,
  `goals` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`player_id`),
  KEY `players_FK` (`user_id`),
  KEY `players_FK_1` (`team_id`),
  CONSTRAINT `players_FK` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `players_FK_1` FOREIGN KEY (`team_id`) REFERENCES `teams` (`team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `matches` (
  `match_id` int(11) NOT NULL AUTO_INCREMENT,
  `team_home` int(11) DEFAULT NULL,
  `team_away` int(11) DEFAULT NULL,
  `tournament_id` int(11) DEFAULT NULL,
  `score_home` int(11) DEFAULT NULL,
  `score_away` int(11) DEFAULT NULL,
  `winner` varchar(15) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`match_id`),
  KEY `matches_FK` (`tournament_id`),
  KEY `matches_FK_1` (`team_home`),
  KEY `matches_FK_2` (`team_away`),
  CONSTRAINT `matches_FK` FOREIGN KEY (`tournament_id`) REFERENCES `tournaments` (`tournament_id`),
  CONSTRAINT `matches_FK_1` FOREIGN KEY (`team_home`) REFERENCES `teams` (`team_id`),
  CONSTRAINT `matches_FK_2` FOREIGN KEY (`team_away`) REFERENCES `teams` (`team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Dados sobre a partida';

CREATE TABLE `lineups` (
  `lineup_id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) DEFAULT NULL,
  `formation` varchar(10) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`lineup_id`),
  KEY `lineups_FK` (`match_id`),
  CONSTRAINT `lineups_FK` FOREIGN KEY (`match_id`) REFERENCES `matches` (`match_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Formação para partida';

CREATE TABLE `linup_starts` (
  `lineup_start_id` int(11) NOT NULL AUTO_INCREMENT,
  `lineup_id` int(11) DEFAULT NULL,
  `player_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`lineup_start_id`),
  KEY `linup_starts_FK` (`lineup_id`),
  KEY `linup_starts_FK_1` (`player_id`),
  CONSTRAINT `linup_starts_FK` FOREIGN KEY (`lineup_id`) REFERENCES `lineups` (`lineup_id`),
  CONSTRAINT `linup_starts_FK_1` FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Os 11 iniciais de cada formação';

CREATE TABLE `goals` (
  `goal_id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` int(11) DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`goal_id`),
  KEY `goals_FK` (`player_id`),
  KEY `goals_FK_1` (`match_id`),
  CONSTRAINT `goals_FK` FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`),
  CONSTRAINT `goals_FK_1` FOREIGN KEY (`match_id`) REFERENCES `matches` (`match_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='tabela de quem marcou os gols';

CREATE TABLE `red_cards` (
  `red_card_id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) DEFAULT NULL,
  `player_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`red_card_id`),
  KEY `red_cards_FK` (`match_id`),
  KEY `red_cards_FK_1` (`player_id`),
  CONSTRAINT `red_cards_FK` FOREIGN KEY (`match_id`) REFERENCES `matches` (`match_id`),
  CONSTRAINT `red_cards_FK_1` FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Cartões vermelhos';

CREATE TABLE `yellow_cards` (
  `yellow_card_id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) DEFAULT NULL,
  `player_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`yellow_card_id`),
  KEY `yellow_cards_FK` (`match_id`),
  KEY `yellow_cards_FK_1` (`player_id`),
  CONSTRAINT `yellow_cards_FK` FOREIGN KEY (`match_id`) REFERENCES `matches` (`match_id`),
  CONSTRAINT `yellow_cards_FK_1` FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `assists` (
  `assit_id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) DEFAULT NULL,
  `player_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`assit_id`),
  KEY `assists_FK` (`match_id`),
  KEY `assists_FK_1` (`player_id`),
  CONSTRAINT `assists_FK` FOREIGN KEY (`match_id`) REFERENCES `matches` (`match_id`),
  CONSTRAINT `assists_FK_1` FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Jogadores que deram assistencias';
