CREATE TABLE `Entry` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `date` DATETIME NOT NULL,
    `concept` TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `mood_id` INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);

CREATE TABLE `Mood` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
)

INSERT INTO `Entry` VALUES (null, "01-4-2021", "HTML & CSS", "We talked about HTML components and how to make grid layouts with Flexbox in CSS.", 4);
INSERT INTO `Entry` VALUES (null, "01-7-2021", "GitHub Workflow", "Worked on indivdual and group project GitHub workflow for pushing branches from command to GitHub", 3);
INSERT INTO `Entry` VALUES (null, "01-14-2021", "JavaScript", "Exporting data from mulitple objects and functions in JavaScript", 4);
INSERT INTO `Entry` VALUES (null, "02-02-2021", "API and fetch", "Introduced to fetch commands and using DATA from an API", 4)
INSERT INTO `Entry` VALUES (null, "03-09-2021", "React", "Installed npm and learned React.js", 4)


INSERT INTO `Mood` VALUES (null, "Sad");
INSERT INTO `Mood` VALUES (null, "Not too great");
INSERT INTO `Mood` VALUES (null, "Okay");
INSERT INTO `Mood` VALUES (null, "Pretty good");
INSERT INTO `Mood` VALUES (null, "Great");