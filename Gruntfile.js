module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    // Concatanation of JS
    concat: {
      options: {
        separator: ';'
      },
      dist: {
        src: [
          '<%= pkg.project_paths.bower_folder %>jquery/dist/jquery.js',
          // '<%= pkg.project_paths.bower_folder %>foundation/js/foundation.js',
          '<%= pkg.src_paths.js %>**/*.js'
        ],
        dest: '<%= pkg.dest_paths.js %>app.js'
      }
    },
    // Minification of JS
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("dd-mm-yyyy") %> */\n'
      },
      dist: {
        files: {
          '<%= pkg.dest_paths.js %>app.js': ['<%= concat.dist.dest %>'],
        }
      },
      dev: {
        files: {
          '<%= pkg.dest_paths.js %>modernizr.min.js': ['<%= pkg.project_paths.bower_folder %>modernizr/modernizr.js']
        }
      }
    },
    // CSSmin to minify CSS on production
    cssmin: {
        minify:{
        expand: true,
        cwd: '<%= pkg.dest_paths.css %>',
        src: ['*.css',],
        dest: '<%= pkg.dest_paths.css %>',
        ext: '.css' 
      }
    },
    // JSHint to review JS code before build
    jshint: {
      files: [
        '<%= pkg.src_paths.js %>**/*.js',
      ],
      options: {
        // options here to override JSHint defaults
        globals: {
          jQuery: true,
          console: true,
          module: true,
          alert: true,
          document: true,
          window:true
        }
      }
    },
    // Compass to handle CSS compilation and concatanation
    compass: {
      dist: {
        options: {
          config: "config.rb"
        }
      }
    },
    // Copy fonts and images to build output directory
    copy: {
      dist: {
        files: [
          // Fonts
          {
            expand: true,
            cwd: '<%= pkg.src_paths.fonts %>',
            src: ['**/*', '!**/*.json'],
            dest: '<%= pkg.dest_paths.fonts %>'
          },
          // Images
          {
            expand: true,
            cwd: '<%= pkg.src_paths.images %>',
            src: '**/*',
            dest: '<%= pkg.dest_paths.images %>'
          }
        ]
      }
    },
    // Watch task to compile files live
    watch: {
      js:{
        files: ['<%= jshint.files %>'],
        tasks: ['jshint', 'concat']
      },
      scss: {
        files: ['<%= pkg.src_paths.scss %>**/**/*.scss'],
        tasks: ['compass']
      },
      images: {
        files: [
          '<%= pkg.src_paths.images %>**/*.jpg',
          '<%= pkg.src_paths.images %>**/*.gif',
          '<%= pkg.src_paths.images %>**/*.png'
        ],
        tasks: ['copy']
      },
      fonts: {
        files: [
          '<%= pkg.src_paths.fonts %>**/*.eot',
          '<%= pkg.src_paths.fonts %>**/*.woff',
          '<%= pkg.src_paths.fonts %>**/*.svg',
          '<%= pkg.src_paths.fonts %>**/*.ttf'
        ],
        tasks: ['copy']
      }
    },
    docco: {
      debug: {
        src: ['<%= pkg.src_paths.js %>**/*.js'],
        options: {
          output: 'docs/js/'
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-compass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-docco');

  grunt.registerTask('default', ['jshint', 'concat', 'uglify:dev', 'compass', 'copy']);
  grunt.registerTask('build', ['jshint', 'concat', 'uglify:dev', 'compass', 'copy']);
  grunt.registerTask('dist', ['jshint', 'concat', 'uglify', 'compass', 'cssmin', 'copy']);
  grunt.registerTask('doc', 'docco');

};