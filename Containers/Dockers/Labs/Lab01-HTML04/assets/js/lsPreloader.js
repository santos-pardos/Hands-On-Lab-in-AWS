


//////////////////////////////////////////////////////////////////////
//				@charset "UTF-8"									//
//				@language ECMASCRIPT5							    //
//				@ Title: Plugin Pré-loader com jQuery				//
//				@ Author: Leonardo Silva							//
//				@ Version: 1.0										//
//				@ Todos os direitos reservados						//
//////////////////////////////////////////////////////////////////////



(function($){
	
	
	//Opções padrão
	var $opLoader = {
						backgroundColor:	"#000",						  		//Cor do background
						backgroundImage:	"",									//Imagem do background
						backgroundRepeat:	"repeat",							//Repetir imagem do background ( repeat | no-repeat | repeat-x | repeat-y )
						logoImage:			"",							  		//Caminho logo
						progressShow:		true,						  		//Mostrar barra de progresso
						progressColor: 		"#FFF",						  		//Cor da barra de progresso
						progressHeight: 	"10px",						  		//Altura da barra de progresso
						progressPosition:	"bottom",					  		//Posição da barra de progresso ( top | center | bottom )
						percentShow:		true,						 		//Mostrar porcentagem do loading
						percentFontFamily:	"Verdana, Geneva, sans-serif",		//Familia da fonte da porcentagem
						percentFontSize:	"50px",							  	//Tamanho da fonte da porcentagem				
						animationComplete: 	"fade",						 		//Efeito fim do preloader ( fade | hide | slideUp | slideDown | slideLeft | slideRight )
						minimumTime:		.5,							  		//Tempo minímo de execução em segundos
						onStart:			function(){},						//Função para ser executada ao iniciar do preloader
						onComplete:			function(){}				  		//Função para ser executada após o termino do preloader
					};
	
	var CONTAINER;				//Armazena o elemento que chama o plugin
	var _urlImages 	= [];		//Armazena as urls das imagens
	
	var startTime;				//Tempo de inicio do pré loader
	var finishTime;				//Tempo da animação do fim do pré loader
	
	var hiddenContainer;		//Div escondida que irá armazenar as imagens pré carregadas
	var imageCount = 0;			//Contador das imagens carregadas
	var imageCalc  = 0;			//Contador das imagens calculadas
	
	var divOverlay;				//Div overlay
	var divBarProgress;			//Div barra de progresso
	var divPercentProgress;		//Div porcentagem do progresso
	var divLogoImage;			//Div logo do parceiro
					
	//Função principal do plugin				
	$.fn.lsPreloader = function( options ){
		
		CONTAINER = this; //Elemento que chama o plugin
		
		if( options ) $.extend( $opLoader, options );	
		
		this.find("*").each( function(){
			
			selectImages( this );
		
		});
		
		createLoader();
		
		return this;
		
	}
	
	//Separa as urls das imagens
	var selectImages = function( element ){
		
		var url = "";

        if( $( element ).css( "background-image" ) != "none" ) var url = $( element ).css( "background-image" ).replace( "url(", "" ).replace( ")", "" );
		else if( typeof ( $( element ).attr( "src" ) ) != "undefined" && element.nodeName.toLowerCase() == "img" ) var url = $( element ).attr( "src" );
		
		if( url != "" ){
			
			 _urlImages.push( url );
		
		}
		
		//console.log( _urlImages );
		
	}
	
	//Cria os elementos do loader
	var createLoader = function(){
		
		var date = new Date();
		startTime = date.getTime();
		
		if( _urlImages != "" ){
			
			 //console.log( "Ok" );
			 
			 createElementsPreLoader();
			 createContainer();
			 
			 $opLoader.onStart();
			 
		}else{
			
			 //console.log( "Not ok" );
			 
			 $opLoader.onComplete();
		
		}
		
	}
	
	//Cria elementos do pré loader
	var createElementsPreLoader = function(){
		
		CONTAINER.css({ overflow: "hidden" });
		
		divOverlay = $( "<div id=\"preloader-overlay\"></div>" )
					 .appendTo( CONTAINER )
					 .css({
						width: CONTAINER.width(),
						height: CONTAINER.height(),
						backgroundColor: $opLoader.backgroundColor,
						backgroundImage: "url(" + $opLoader.backgroundImage + ")",
						backgroundRepeat: $opLoader.backgroundRepeat,
						backgroundPosition: "fixed",
						position: "fixed",
						zIndex: 999999,
						top: CONTAINER.offset().top,
						left: CONTAINER.offset().left						 
					  });
		
		if( $opLoader.progressShow ){
					  
			divBarProgress = $( "<div id=\"preloader-bar-progress\"></div>" )
							 .appendTo( divOverlay )
							 .css({
								width: "0%",
								height: $opLoader.progressHeight,
								backgroundColor: $opLoader.progressColor,
								position: "absolute",
								left: 0
							  });
							  
			switch( $opLoader.progressPosition ){
				
				case "top":
						
						divBarProgress.css({ top: 0, marginTop: 0 });
						
					break;
					
				case "center":
						
						divBarProgress.css({ top: "50%", marginTop: "-" + ( parseFloat($opLoader.progressHeight) / 2 ) + "px" });
						
					break;
					
				case "bottom":
						
						divBarProgress.css({ bottom: 0, marginBottom: 0 });
						
					break;
					
			}
		
		}
						  
		if( $opLoader.percentShow ){
						  
			divPercentProgress = $( "<div id=\"preloader-percent-progress\"></div>" )
								 .appendTo( divOverlay )
								 .css({
									width: "200px",
									height: $opLoader.percentFontSize,
									position: "absolute",
									top: "50%",
									left: "50%",
									marginTop: ( parseFloat($opLoader.progressHeight) / 2 ) + 15 + "px",
									marginLeft: "-100px",
									fontFamily: "Verdana, Geneva, sans-serif",
									fontSize: $opLoader.percentFontSize,
									fontWeight: "bold",
									color: $opLoader.progressColor,
									textAlign: "center",
									lineHeight: $opLoader.percentFontSize
								  })
								  .html("0%");
							  
		}
		
		if( $opLoader.logoImage != "" ){
								  
			divLogoImage = $( "<div id=\"preloader-logo-image\"></div>" )
						   .appendTo( divOverlay )
						   .css({
							  width: "100%",
							  height: "100%", 
							  position: "absolute",
							  bottom: "50%",
							  left: "0",
							  marginBottom: ( parseFloat($opLoader.progressHeight) / 2 ) + 20 + "px",
							  backgroundImage: "url(" + $opLoader.logoImage + ")",
							  backgroundPosition: "center bottom",
							  backgroundRepeat: "no-repeat"
						   });
						   
		}
		
	}
	
	//Cria div escondida para carregar as imagens
	var createContainer = function(){
		
		hiddenContainer = $( "<div></div>" ).appendTo( CONTAINER )
										  	.css({
													display: "none",
													overflow: "hidden",
													width: 0,
													height: 0													
											  	});
		
		for( var i = 0; i < _urlImages.length; i++ ){
			
			
			var image = new Image();
			
			$( image ).one({
				
				load: function(){
					
					//Success - Imagem carregada
					//console.log("Carregou imagem");
					timePercent();	
					
				},
				
				error: function(){
					
					//Error - Imagem está em cache no navegador
					//console.log("Imagem em cache");
					timePercent();
					
				}
			
			})
			.attr( "src", _urlImages[i] )
			.appendTo( hiddenContainer );
			
			/*$( image )
			.load( function() {
				
				//Success
				console.log("Carregou");
				timePercent();
				
			} )
			.error( function() {
				
				//Error - Imagem está em cache no navegador
				console.log("Imagem em cache");
				timePercent();
				
			} )
			.attr( "src", _urlImages[i] )
			.appendTo( hiddenContainer );*/
			
		}
		
	}
	
	//Calcula o tempo e porcentagem para carregar imagem
	var timePercent = function(){
		
		imageCount++;
		
		var percent = ( imageCount / _urlImages.length ) * 100 ;
		
		if( $opLoader.progressShow ){
			
			divBarProgress.stop().animate({
											width: percent + "%",
											minWidth: percent + "%",
										  }, 400);
			
		}
									  
		if( $opLoader.percentShow ) divPercentProgress.text( Math.ceil( percent ) + "%" );
		
		if( imageCount == _urlImages.length ) destroyLoader();
		
	}
	
	//Destroi o loader e carrega a página
	var destroyLoader = function(){
		
		//console.log( "Destruir" );
		
		hiddenContainer.remove();
		animateOutPreLoader();
		
	}
	
	//Animações do onComplete
	var animateOutPreLoader = function(){
		
		finishTime = $opLoader.minimumTime * 1000;
		
		var date = new Date();
		
		if( ( date.getTime() - startTime ) < finishTime ) finishTime = ( finishTime - ( date.getTime() - startTime ) );
		
		switch( $opLoader.animationComplete ){
			
			case "fade":
				
				divOverlay.delay( finishTime )
				.fadeOut( 500, function(){ 
											
											functionOutPreLoader();
										
										 } );
				
				break;
				
			case "hide":
				
				divOverlay.delay( finishTime )
				.hide( 0, function(){
										
										functionOutPreLoader();
									
									 });
				
				break;
				
			case "slideUp":
				
				divOverlay.delay( finishTime )
				.css( { position: "absolute" } )
				.animate( { top: "-=100%" }, 500, function(){
																
																functionOutPreLoader();
												
															 } );
				
				break;
			
			case "slideDown":
				
				divOverlay.delay( finishTime )
				.css( { position: "absolute" } )
				.animate( { top: "+=100%" }, 500, function(){
																
																functionOutPreLoader();
												
															 } );
				
				break;
				
			case "slideLeft":
				
				divOverlay.delay( finishTime )
				.css( { position: "absolute" } )
				.animate( { left: "-=100%" }, 500, function(){
																
																functionOutPreLoader();
												
															 } );
				
				break;
				
			case "slideRight":
				
				divOverlay.delay( finishTime )
				.css( { position: "absolute" } )
				.animate( { left: "+=100%" }, 500, function(){
																
																functionOutPreLoader();
												
															 } );
				
				break;
				
		} 
		
	}
	
	//Função executada após animação do onComplete
	var functionOutPreLoader = function(){
		
		$( CONTAINER ).removeAttr("style");
		divOverlay.remove(); 
		$opLoader.onComplete();
		
	}
	
	
})(jQuery);
